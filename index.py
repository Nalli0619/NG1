from nicegui import ui,app
import os
avatar_dir = 'C:/Users/曾伟恒/OneDrive/Desktop/NG'
app.add_static_files('/avatars', local_directory=avatar_dir)
with ui.chat_message(name='我补药回答问题', stamp="now", avatar='/avatars/微信图片_2025-11-22_172847_113.jpg'):
    ui.image('C:/Users/曾伟恒/OneDrive/Desktop/NG/屏幕截图 2025-11-22 194437.png')
    ui.image('C:/Users/曾伟恒/OneDrive/Desktop/NG/屏幕截图 2025-11-22 194813.png')
    ui.label("tqz看猫猫")
with ui.dropdown_button('来摸猫猫', auto_close=True):
    ui.item('一号猫猫', on_click=lambda: ui.notify('我我我！'))
    ui.item('二号猫猫', on_click=lambda: ui.notify('我帅的要命'))
ui.link("别戳这个","https://www.identityvgame.com/tw/")
ui.run()