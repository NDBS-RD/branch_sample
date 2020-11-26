'use scrict';

// 行動履歴詳細ボタン押下イベント
$('#historyDetail').on('click', function() {
  showFunctionList();
});

function showFunctionList() {
  window.open('/historyDetail', 'historyDetail', '');
};