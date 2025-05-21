# Gemini API Python Request Script

This script sends a request to the Google Gemini API using the Python SDK.

## Prerequisites

- Python 3.7+
- A Google Cloud Project with the Vertex AI API enabled.
- Authenticated `gcloud` CLI.

## Setup

1.  **Install the Google Generative AI SDK:**
    ```bash
    pip install google-generativeai
    ```

2.  **Authenticate with Google Cloud:**
    If you haven't already, authenticate your gcloud CLI. This script uses Application Default Credentials.
    ```bash
    gcloud auth application-default login
    ```
    Ensure the authenticated user has the necessary permissions (e.g., "Vertex AI User" role) on the Google Cloud project.

## Running the Script

1.  **Clone the repository (if you haven't already).**
2.  **Navigate to the script directory.**
3.  **Run the script:**
    ```bash
    python gemini_request.py "日本の天気について教えてください。"
    ```
    Replace `"日本の天気について教えてください。"` with your desired prompt.
    The script will send the provided prompt to the Gemini API and print the response.

## Customization

-   **Prompt:** The prompt is provided as a command-line argument when running the script. See 'Running the Script' for an example.
-   **Model:** The script uses `gemini-1.5-flash-latest` by default. You can change the `model_name` argument in the `send_gemini_request` function call or its default value to use a different Gemini model.
