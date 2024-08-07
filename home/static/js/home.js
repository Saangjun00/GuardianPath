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