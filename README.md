<br>
<p align='center'>
<img src='assets\meta\github_demo_pfp.png' width='250px'/>
</p>
<h1 align='center'>AvatarGen</h1>

<h6 align='center'>Image Manipulation Bot for Telegram.</h6>

<br>

My instance (might not be up): <a href='https://t.me/AvatarGen_bot'>@AvatarGen_bot</a>

Telegram bot which does image manipulation on the fly on users' commands. At the back it uses <a href='https://github.com/prashantrahul141/ImageEffects'>prashantrahul141/<b>ImageEffects</b></a> library. Type <a href='https://t.me/AvatarGen_bot?start=help'>/help </a> for help.

<h3> Hosting your own instance </h3>

1. Create a telegram bot using <a href='https://t.me/BotFather'>@BotFather</a> and get its TOKEN.

2. Clone the repo

```sh
git clone https://github.com/prashantrahul141/AvatarGen
```

3. Put these in .env

```sh
TOKEN=YOUR BOT TOKEN
# DEV_ID_0=Each dev ids ( Telegram user id ) # Optional
# DEV_ID_1=Each dev ids ( Telegram user id ) # Optional
```

4. Install dependencies

```sh
pip install -r requirements.txt
```

5. Run `main.py`

```sh
python main.py
```
