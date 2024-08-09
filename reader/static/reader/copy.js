// Получаем все кнопки "Копировать"
var copyButtons = document.querySelectorAll('.copy_button');

// Для каждой кнопки добавляем обработчик события click
copyButtons.forEach(function(button) {
    button.addEventListener('click', function() {
        // Получаем текст из соответствующего блока с адресом
        var addressText = this.parentNode.querySelector('.title_fc').textContent.trim();

        // Копируем текст в буфер обмена
        navigator.clipboard.writeText(addressText).then(function() {
            // Показываем сообщение "Скопировано"
            var copyMessage = document.getElementById('copyMessage');
            copyMessage.classList.add('show');
            // Устанавливаем таймер для плавного исчезновения
            setTimeout(function() {
                copyMessage.classList.remove('show');
            }, 3000);
        }).catch(function(error) {
            console.error('Не удалось скопировать текст: ', error);
        });
    });
});
