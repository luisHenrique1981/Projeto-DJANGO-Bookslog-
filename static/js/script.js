function abrir_nav() {
    document.getElementById('menu-lateral').classList.add('show');
}

function fechar_nav() {
    document.getElementById('menu-lateral').classList.remove('show');
}


document.querySelectorAll('.caixa-resp').forEach(function (pergunta) {
    pergunta.addEventListener('click', function () {
        let resposta = this.nextElementSibling;
        let icon = this.querySelector('i');

        if (resposta.style.display === 'block') {
            resposta.style.display = 'none';
            icon.style.transform = 'rotate(0deg)'; // Volta o ícone para a posição original
        } else {
            resposta.style.display = 'block';
            icon.style.transform = 'rotate(180deg)'; // Rotaciona o ícone
        }
    });
});


function setupTabs () {
    document.querySelectorAll(".tabs__button").forEach(button => {
        button.addEventListener("click", () => {
            const sideBar = button.parentElement;
            const tabsContainer = sideBar.parentElement;
            const tabNumber = button.dataset.forTab;
            const tabToActivate = tabsContainer.querySelector('.tabs__content[data-tab="${tabNumber}"]');

            sideBar.querySelectorAll(".tabs__button").forEach(button => {
                button.classList.remove("tabs__button--active");
            });

            tabsContainer.querySelectorAll(".tabs__content").forEach(tab => {
                tab.classList.remove("tabs__content--active");
            });

            button.classList.add("tabs__button--active");
            tabToActivate.classList.add("tabs__content--active");
        });
    });
}

document.addEventListener("DOMContentLoaded", () => {
    setupTabs();

    document.querySelectorAll('.tabs').forEach(tabsContainer => {
        tabsContainer.querySelector(".tabs__sidebar .tabs__button").click();
    })
});