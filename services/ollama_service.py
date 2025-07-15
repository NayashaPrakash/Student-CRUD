import requests

class OllamaService:
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url

    def generate_student_summary(self, student):
        try:
            prompt = f"""Generate a brief, professional summary for the following student profile:

            Name: {student['name']}
            Age: {student['age']}
            Email: {student['email']}
            Account Created: {student['created_at']}
            Last Updated: {student['updated_at']}

            Please provide a concise summary that includes:
            1. A brief introduction
            2. Key characteristics based on the available information
            3. Potential academic insights or recommendations

            Keep the response under 200 words and make it informative yet personable."""

            payload = {
                "model": "llama3.2",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant that writes professional student summaries."},
                    {"role": "user", "content": prompt}
                ],
                "stream": False
            }

            response = requests.post(f'{self.base_url}/api/chat',
                                     json=payload,
                                     timeout=60)


            if response.status_code == 200:
                # return response.json().get('response', 'Summary generation failed')
                data = response.json()
                return data.get('message', {}).get('content', 'Summary generation failed')

            else:
                return f"Error: Unable to generate summary (Status: {response.status_code})"

        except requests.exceptions.ConnectionError:
            return "Error: Unable to connect to Ollama. Please ensure Ollama is running on localhost:11434"
        except requests.exceptions.Timeout:
            return "Error: Request timeout. Ollama took too long to respond"
        except Exception as e:
            return f"Error: {str(e)}"

# Create global instance
ollama_service = OllamaService()
