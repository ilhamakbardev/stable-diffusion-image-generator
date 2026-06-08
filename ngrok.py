from pyngrok import ngrok
import subprocess

auth_token = "cr_3B4kT2Zu2hgwsxRLG7Kdokg2gU8"

ngrok.set_auth_token(auth_token)
subprocess.Popen(["streamlit", "run", "app.py"])

ngrok.kill()
public_url = ngrok.connect(8501).public_url
print(public_url)