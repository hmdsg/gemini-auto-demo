import google.generativeai as genai
import argparse

def send_gemini_request(prompt_text: str, model_name: str = "gemini-1.5-flash-latest") -> str:
  """Sends a request to the Gemini API and returns the response text.

  Args:
    prompt_text: The text prompt to send to the model.
    model_name: The name of the Gemini model to use.

  Returns:
    The text content of the model's response.
  """
  try:
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt_text)
    return response.text
  except Exception as e:
    print(f"An error occurred in send_gemini_request: {e}")
    return ""

if __name__ == "__main__":
  # Note: To run this script, you need to have the GOOGLE_API_KEY environment
  # variable set to your API key.
  parser = argparse.ArgumentParser(description="Send a prompt to the Gemini API.")
  parser.add_argument("prompt", help="The prompt text to send to the Gemini API")
  args = parser.parse_args()

  try:
    response_text = send_gemini_request(args.prompt)
    if response_text:
      print(response_text)
  except Exception as e:
    print(f"An error occurred in main: {e}")
    print("Please ensure you have the GOOGLE_API_KEY environment variable set.")
    print("You can get an API key from https://aistudio.google.com/app/apikey")
