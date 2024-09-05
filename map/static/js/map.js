var map;
function initTmap() {
    // Tmap 지도 생성
    map = new Tmapv2.Map("map_div", {
        center: new Tmapv2.LatLng(37.5665, 126.9780), // 서울 시청 좌표 (샘플)
        width: "100%",
        height: "500px",
        zoom: 15
    });

    // 출발지와 도착지 마커 표시
    var markerStart = new Tmapv2.Marker({
        position: new Tmapv2.LatLng(37.5665, 126.9780), // 출발지 좌표 (샘플)
        map: map
    });

    var markerEnd = new Tmapv2.Marker({
        position: new Tmapv2.LatLng(37.5765, 126.9880), // 도착지 좌표 (샘플)
        map: map
    });

    // 경로 그리기 로직 추가 가능
}

// 페이지 로드 후 지도 초기화
window.onload = function () {
    initTmap();
}