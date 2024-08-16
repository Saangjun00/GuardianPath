function toggleProfilePanel() {
    var panel = document.getElementById('profile-panel');
    if (panel.style.display === 'block') {
        panel.style.display = 'none';
    } else {
        panel.style.display = 'block';
    }
}

// 클릭이 다른 곳에서 발생했을 때 패널 닫기
document.addEventListener('click', function(event) {
    var profileIcon = document.querySelector('.profile-icon-btn');
    var panel = document.getElementById('profile-panel');
    if (!profileIcon.contains(event.target) && !panel.contains(event.target)) {
        panel.style.display = 'none';
    }
});

function toggleProfilePanel() {
    var profilePanel = document.getElementById('profile-panel');
    if (profilePanel.style.display === 'block') {
        profilePanel.style.display = 'none';
    } else {
        profilePanel.style.display = 'block';
    }
}

// 클릭 시 메뉴 바깥을 클릭하면 메뉴가 닫히도록
document.addEventListener('click', function(event) {
    var profilePanel = document.getElementById('profile-panel');
    var profileIconBtn = document.querySelector('.profile-icon-btn');
    if (!profilePanel.contains(event.target) && !profileIconBtn.contains(event.target)) {
        profilePanel.style.display = 'none';
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var messages = document.querySelectorAll('.messages .alert');
    messages.forEach(function(message) {
        setTimeout(function() {
            message.classList.add('hidden'); // hidden 클래스를 추가하여 opacity를 0으로 만들고, display를 none으로 변경
            setTimeout(function() {
                message.remove(); // 요소를 DOM에서 제거
            }, 1000); // 1초 후에 요소 제거 (transition 시간과 일치하도록 조정)
        }, 3000); // 3초 후에 애니메이션 시작
    });
});

function openAddressSearch(fieldId) {
    new daum.Postcode({
        oncomplete: function(data) {
            var address = data.roadAddress || data.jibunAddress;
            document.getElementById(fieldId).value = address;
        }
    }).open();
}