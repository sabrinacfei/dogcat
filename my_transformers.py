from transformers import AutoModelForCausalLM, AutoTokenizer

# 替换为你选择的模型名称
model_name = "gpt2"  # 例如使用你下载的模型名称

# 加载模型和 tokenizer
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 输入文本
input_text = "你想和模型聊天吗？"

# 编码输入文本
inputs = tokenizer(input_text, return_tensors="pt")

# 使用模型生成响应
outputs = model.generate(**inputs)

# 解码生成的响应文本
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# 打印生成的文本
print(response)
