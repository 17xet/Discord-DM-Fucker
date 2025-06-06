# Discord DM Fucker 🤖✉️

A Python tool that sends DMs to a specific user from multiple Discord bot tokens in parallel.

![Screenshot 2025-06-05 182326](https://github.com/user-attachments/assets/69247e36-c0a0-4ddd-bb2d-b8885bc0f9c2)


> ⚠️ This tool is for **educational and testing purposes only**. Abuse of this tool may violate Discord's [Terms of Service](https://discord.com/terms).

---

## ✨ Features

- Load multiple bot tokens from a `tokens.json` file
- Send a custom message multiple times to a user
- Colored terminal UI using `pystyle`
- Async-powered using `discord.py`

---

## 📦 Requirements

Install required packages with:

```bash
pip install -r requirements.txt
````

---

## 📄 requirements.txt

```text
discord.py
pystyle
```

---

## 🚀 Usage

1. Create a `tokens.json` file with this format:

```json
[
    "BOT_TOKEN_1",
    "BOT_TOKEN_2",
    "BOT_TOKEN_3"
]
```

2. Run the script:

```bash
python bot_messenger.py
```

3. You will be prompted to enter:

   * User ID to send messages to
   * File name of your token list (e.g. `tokens.json`)
   * Message to send
   * Number of times to send it

---

## 👁 Preview

```text
Enter the user ID to message: 123456789012345678
Enter the bot token file name (e.g., tokens.json): tokens.json
Enter the message to send: Hello from all my bots!
Enter how many times to send the message: 3

Bot1 successfully sent messages.
Bot2 successfully sent messages.
...
```

---

## 🙏 Credits

Made with ❤️ by [17xet](https://github.com/17xet)
📺 [YouTube - @17xet](https://www.youtube.com/@17xet)
🧩 [Discord - mx9raXzU9S](https://discord.gg/mx9raXzU9S)

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.
---

