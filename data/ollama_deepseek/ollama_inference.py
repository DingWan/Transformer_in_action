import requests
import json

def split_response(full_response):
    """将完整响应拆分为推理过程和生成结果（示例逻辑：按第一个换行符分割）"""
    if "\n\n" in full_response:
        reasoning, generation = full_response.split("\n\n", 1)
    else:
        reasoning = full_response
        generation = "[未检测到明显结果分隔]"
    return reasoning.strip(), generation.strip()

def call_ollama(stream=False):
    # 获取用户输入
    prompt = input("\n请输入您的问题：")
    if not prompt.strip():
        return "错误：输入不能为空"

    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "deepseek-r1:7b",
        "prompt": f"请先进行推理分析，再给出最终答案。问题：{prompt}",
        "stream": stream,
        "options": {"temperature": 0.7}
    }

    try:
        if stream:
            full_response = []
            with requests.post(url, json=payload, stream=True) as resp:
                resp.raise_for_status()
                print("\n【实时流式输出】")
                for line in resp.iter_lines():
                    if line:
                        chunk = json.loads(line.decode("utf-8"))
                        token = chunk.get("response", "")
                        print(token, end="", flush=True)
                        full_response.append(token)
            full_text = "".join(full_response)
        else:
            resp = requests.post(url, json=payload)
            resp.raise_for_status()
            full_text = resp.json()["response"]
        
        # 拆分结果
        reasoning, generation = split_response(full_text)
        return {
            "用户问题": prompt,
            "推理结果": reasoning,
            "生成结果": generation
        }

    except requests.exceptions.ConnectionError:
        return {"错误": "无法连接到Ollama服务，请确认服务已启动"}
    except Exception as e:
        return {"错误": str(e)}

if __name__ == "__main__":
    # 非流式调用示例
    print("\n=== 非流式模式 ===")
    result = call_ollama(stream=False)
    if "推理结果" in result:
        print("\n【推理过程】\n", result["推理结果"])
        print("\n【最终答案】\n", result["生成结果"])
    else:
        print("错误：", result)

    # 流式调用示例
    print("\n=== 流式模式 ===")
    result = call_ollama(stream=True)
    if "推理结果" in result:
        print("\n\n【完整推理过程】\n", result["推理结果"])
        print("\n【完整生成结果】\n", result["生成结果"])
    else:
        print("错误：", result)