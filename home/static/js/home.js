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