# import gradio as gr
# import google.generativeai as genai

# # Configure API Key
# genai.configure(api_key="AIzaSyDFXWa0ZzUjqCTERYQ_2peRXedFLz6EM8A")

# # Function to interact with Gemini AI
# def chat_with_gemini(prompt):
#     model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Updated model name
#     response = model.generate_content(prompt)
#     return response.text

# # Create a Gradio interface
# iface = gr.Interface(
#     fn=chat_with_gemini,
#     inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
#     outputs="text",
#     title="Chat with Gemini AI",
#     description="Ask anything, and Gemini AI will respond!"
# )

# # Run the Gradio app with public access
# if __name__ == "__main__":
#     iface.launch(share=True)  # Enable public sharing

import gradio as gr

# Custom CSS
custom_css = """
<style>
  body {
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(to right, #141e30, #243b55);
      color: white;
  }
  .gradio-container {
      max-width: 600px;
      margin: auto;
      padding: 20px;
      border-radius: 15px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(10px);
  }
  .gradio-container input, .gradio-container select, .gradio-container button {
      font-size: 16px;
      padding: 10px;
      border-radius: 8px;
      border: none;
      outline: none;
      transition: all 0.3s ease-in-out;
  }
  .gradio-container button:hover {
      background: #ff9800;
      color: white;
      transform: scale(1.05);
  }
</style>
"""

# Custom JavaScript
custom_js = """
<script>
  document.addEventListener("DOMContentLoaded", function() {
      document.querySelectorAll("button").forEach(button => {
          button.addEventListener("mouseover", () => {
              button.style.boxShadow = "0 4px 10px rgba(255,152,0,0.5)";
          });
          button.addEventListener("mouseleave", () => {
              button.style.boxShadow = "none";
          });
      });
  });
</script>
"""

blocks = gr.Blocks(css=custom_css, js=custom_js)

with blocks as demo:
    gr.HTML("<h2 style='text-align: center;'>🌟 Interactive Sentence Maker 🌟</h2>")
    subject = gr.Textbox(placeholder="Enter Subject (e.g. The cat)")
    verb = gr.Radio(["ate", "loved", "hated"])
    object = gr.Textbox(placeholder="Enter Object (e.g. the cake)")

    with gr.Row():
        btn = gr.Button("Create Sentence 📝")
        reverse_btn = gr.Button("Reverse Sentence 🔄")
        foo_bar_btn = gr.Button("Append 'Foo' ➕")
        reverse_then_to_the_server_btn = gr.Button("Reverse & Send 🚀")

    def sentence_maker(w1, w2, w3):
        return f"{w1} {w2} {w3}"

    output1 = gr.Textbox(label="Generated Sentence")
    output2 = gr.Textbox(label="Reversed Sentence")
    output3 = gr.Textbox(label="Reversed Verb")
    output4 = gr.Textbox(label="Processed & Sent to Backend")

    btn.click(sentence_maker, [subject, verb, object], output1)
    reverse_btn.click(None, [subject, verb, object], output2, js="(s, v, o) => o + ' ' + v + ' ' + s")
    verb.change(lambda x: x, verb, output3, js="(x) => [...x].reverse().join('')")
    foo_bar_btn.click(None, [], subject, js="(x) => x + ' foo'")
    reverse_then_to_the_server_btn.click(
        sentence_maker, [subject, verb, object], output4,
        js="(s, v, o) => [s, v, o].map(x => [...x].reverse().join(''))"
    )

demo.launch()
