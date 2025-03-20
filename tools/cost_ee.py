import sys

def parse_arguments():
    if len(sys.argv) != 4:
        print("Usage: python cost_ee.py <input_chars> <output_chars> <language>")
        print("<input_chars>: Number of input characters (integer)")
        print("<output_chars>: Number of output characters (integer)")
        print("<language>: 'c' for Chinese or 'e' for English")
        sys.exit(1)

    try:
        input_chars = int(sys.argv[1])
        output_chars = int(sys.argv[2])
    except ValueError:
        print("Error: <input_chars> and <output_chars> must be integers.")
        sys.exit(1)

    language = sys.argv[3].lower()
    if language not in ("c", "e"):
        print("Error: <language> must be 'c' (Chinese) or 'e' (English).")
        sys.exit(1)

    return input_chars, output_chars, "zh" if language == "c" else "en"

input_chars, output_chars, language = parse_arguments()

def estimate_openai_cost(input_chars, output_chars, language):
    print(f"Function Parameters: input_chars={input_chars}, output_chars={output_chars}, language={language}")
    # Token estimation
    if language == "zh":  # Chinese: 1 character ≈ 1 token
        input_tokens = input_chars
        output_tokens = output_chars
        # OpenAI GPT-4.5 pricing per 1M tokens
        input_price_per_million = 0.5
        output_price_per_million = 8
    else:  # English: 4 chars ≈ 1 token
        input_tokens = input_chars // 4
        output_tokens = output_chars // 4
        # OpenAI GPT-4.5 pricing per 1M tokens
        input_price_per_million = 75
        output_price_per_million = 150        

    # Calculate cost
    input_cost = (input_tokens / 1_000_000) * input_price_per_million
    output_cost = (output_tokens / 1_000_000) * output_price_per_million
    total_cost = input_cost + output_cost

    # Print results
    print(f"Estimated Cost for GPT-4.5 API:")
    print(f"- Input Tokens: {input_tokens} (Cost: {input_cost:.6f})")
    print(f"- Output Tokens: {output_tokens} (Cost: {output_cost:.6f})")
    print(f"\033[95m→ Total Estimated Cost: {total_cost:.6f}\033[0m")

    print(f"- Input Tokens: {input_tokens} (Cost for 1k queries: {input_cost*1000:.6f})")
    print(f"- Output Tokens: {output_tokens} (Cost for 1k queries: {output_cost*1000:.6f})")
    print(f"\033[95m→ Total Estimated Cost for 1k queries: {total_cost*1000 :.6f}\033[0m")

# Example Usage
#estimate_openai_cost(input_chars=200, output_chars=500, language="zh")  # Chinese example
#estimate_openai_cost(input_chars=800, output_chars=2000, language="en")  # English example
estimate_openai_cost(input_chars, output_chars, language)  # English example