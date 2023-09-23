from gradio_client import Client

client = Client("http://192.168.2.63:7860")
#client.view_api()
# string of dict for input
#kwargs = dict(instruction_nochat='Who are you?')
res = client.predict(api_name="/system_info")
print(res)

# string of dict for output
# response = ast.literal_eval(res)['response']
# assert 'I am h2oGPT' in response or "I'm h2oGPT" in response or 'I’m h2oGPT' in response


# string of dict for input
kwargs = dict(instruction_nochat='Tell me about chicken.')
response = client.predict(str(dict(kwargs)), api_name='/submit_nochat_api')

print(response)


# string of dict for output
# response = ast.literal_eval(res)['response']
#assert 'I am h2oGPT' in response or "I'm h2oGPT" in response or 'I’m h2oGPT' in response