# 🤖 Telegram Bot

[![AWS](https://img.shields.io/badge/Project-Build%20with%20♥-blue?style=for-the-badge&logo=Python)](https://github.com/dennis-hammerschmidt/telegram-bot)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=Telegram)](https://github.com/dennis-hammerschmidt/telegram-bot)
[![AWS](https://img.shields.io/badge/Build%20with-AWS%20Lambda-important?style=for-the-badge&logo=Amazon-AWS)](https://github.com/dennis-hammerschmidt/telegram-bot)
[![Serverless](https://img.shields.io/badge/Serverless-Powered-red?style=for-the-badge&logo=Serverless)](https://github.com/dennis-hammerschmidt/telegram-bot)

## 📬 Purpose

Imagine this: You have several hundred falshcards that you either want to study for an upcoming test or for concepts that you want to repeat again and again. The problem is, you rarely sit down and work your way through them. A better way to make use of your flashcards would be to get them sent right to your phone. This is the purpose of our Telegram bot: Sending you flashcards (or any kind of images) on a scheduled time right to your Telegram chat!

## 🛠 How we build it

The bot is programmed in python 3.7 and uses the serverless framework for AWS Lambda to schedule when the photo should be sent automatically. 

The Telegram bot framework consists of three main components: 

- `handler.py` that stores the python function to send the photo using the python-telegram-bot API
- `serverless.yml` a small serverless file that sends the python function to AWS lambda
- a folder containing your locally stored flashcards (not included in this repo)

## 🗃 How you can use it for your own flashcards!

### 🧰 What you need

- Node.js
- Python 3.7
- Telegram
- AWS account

We will walk you through the steps and let you know when you need them. Everything that comes with the `< ... >` signs (incl. the signs themselves) needs to be replaced by your own credentials.

In order to run the bot for your own flashcards, you can either fork and clone the repository and adjust the files to your needs or you run the following lines in your terminal to set up the serverless framework that you can then populate and adjust to your needs. To make sure the framework is set up correctly, we recommend to follow the second approach (if you don't have it already, install Node.js to execute `npm`). 

```
npm install -g serverless
serverless create --template aws-python3 --path <PATH-TO-YOUR-ROOT-DIRECTORY-OF-THE-BOT>
```

Also make sure to also have a Telegram account (obviously), Python 3.7 installed on your machine and an AWS account with admin rights (you can get a free tire version right [here](https://aws.amazon.com)). 

- Make sure to store your own flashcards (as a `.png`, `.jpeg`, etc.) in a new folder in the root of this project and set the path to `'flashcards_folder/'`.
- Add this path in the `handler.py` file and add the chat ID of the chat where your bot should send the flashcards to. [Here](https://stackoverflow.com/a/32572159) is a description how to get your chat ID.
- The bot in this repo is scheduled to run at 6am and 6pm UTC time. In order to schedule your bot to run at a different (or at multiple other) time points, you can adjust the `cron` function in the `serverless.yml`. Take a look at the [official documentation on AWS](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-expressions.html) for the different options how to schedule a message.

## 🚀 How to deploy your telegram bot to AWS Lambda

You first need to set up a new AWS user and get the respective credentials. [This blog post](https://hackernoon.com/serverless-telegram-bot-on-aws-lambda-851204d4236c) provides a great overview of the steps you need to take.

Once you have your credentials, you need to export them using:

```
export AWS_ACCESS_KEY_ID=<ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<SECRET_ACCESS_KEY>
```

To make sure that the `python-telegram-bot` API gets installed, run the following command in your terminal to execute the `requirements.txt` file (if you set up the project using the serverless method, you may need to add this file manually).

```
pip install -r requirements.txt -t vendored
```

Once you're done, you're ready to deploy your bot to AWS.

```
serverless deploy
``` 

You'll receive an endpoint link that will later be used to set a webhook.

The final step is to connect your bot with the chat in Telegram and to set a webhook. For this, set up a new Telegram bot by messaging @BotFather in Telegram with `/newbot` and follow the instructions. You'll get a Telegram token that you need to export in the terminal using

```
export TELEGRAM_TOKEN="<YOUR_TELEGRAM_TOKEN>"
```

To set a webhook add the endpoint URL you received from the `serverless deploy` and 

```
curl --request POST --url https://api.telegram.org/bot<YOUR_TELEGRAM_TOKEN>/setWebhook --header 'content-type: application/json' --data '{"url": "<ENDPOINT_FROM_SERVERLESS_DEPLOY>"}'
```

After deploying one more time using ```serverless deploy``` you're ready to go and get your own flashcards right into your Telegram chat at your preferred time 🥳
