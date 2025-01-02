import openai
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# تنظیمات API
openai.api_key = "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"

# تابع برای دکمه‌ها
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        ["پرسش و پاسخ 🧠", "راهنما 📖"],
        ["کانال 📢", "پشتیبانی 👤"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(
        "سلام! به بات محمدی خوش آمدید. لطفاً یکی از گزینه‌ها را انتخاب کنید:",
        reply_markup=reply_markup
    )

# تابع برای مدیریت پیام‌های کاربر
def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text

    if user_message == "کانال 📢":
        update.message.reply_text("📢 کانال ما: @MohammadiBots")
    elif user_message == "پشتیبانی 👤":
        update.message.reply_text("👤 پشتیبانی: @AqaiMohammadi")
    elif user_message == "راهنما 📖":
        update.message.reply_text("📖 شما می‌توانید سوالات خود را از بات بپرسید یا از دکمه‌ها استفاده کنید.")
    else:
        # ارسال پیام کاربر به ChatGPT API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_response = response['choices'][0]['message']['content']
        update.message.reply_text(bot_response)

# راه‌اندازی بات
def main():
    TOKEN = "7829017035:AAFPDgieySGSEBJ2VyCotPHPc47hMilSRMY"
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
