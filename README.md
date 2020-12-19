Template project electronic library

https://www.styleshout.com/templates/preview/Abstract_2_0_0/index.html

Пока только электронные книги поддерживаются


SuperUser: admin admin

Отладочные сообщения (материал скрыт и т.д.) передаются в отдельный html - переделать в home с сообщениями


Header: 
Home, 
(login, reset password) or (logout, change password),
Category,

When resetting password, password is changed and new generated password is sent to user email.

May be instead of form.cleaned_data[''] we should use form.cleaned_data.get('', '')?