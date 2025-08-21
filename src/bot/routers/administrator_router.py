from aiogram import Router, F
from aiogram.types import Message


router = Router(name=__name__)


@router.message(F.text.lower() == "айди")
async def send_file_id(message: Message):
    file_id = "none"
    repl = message.reply_to_message
    if repl is None:
        return
    if repl.photo:
        file_id = repl.photo[-1].file_id
    elif repl.audio:
        file_id = repl.audio.file_id
    elif repl.animation:
        file_id = repl.animation.file_id
    if repl.video:
        file_id = repl.video.file_id
    elif repl.sticker:
        file_id = repl.sticker.file_id

    await message.answer(f"{file_id}")
