'use scrict';

// 行動履歴詳細ボタン押下イベント
$('#historyDetail').on('click', function() {
  showFunctionList();
});

function showFunctionList() {
  window.open('/historyDetail', 'historyDetail', '');
};

/*************************************
 * 表にレコード追加
 * 説明：入力フォームの内容を表に１行追加する
 * 引数：なし
 * 戻り値：なし
 *************************************/
function addTableRow() {

  // 表のオブジェクト取得
  var table = document.getElementById('params');

  // 行末に行(tr要素)追加
  var row = table.insertRow(-1);

  // セル(td要素)の追加
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);
  var cell4 = row.insertCell(3);
  var cell5 = row.insertCell(4);
  var cell6 = row.insertCell(5);
  var cell7 = row.insertCell(6);
  var cell8 = row.insertCell(7);
  var cell9 = row.insertCell(8);

  // セルにデータを挿入 ※入力フォームからデータ取得
  cell1.innerHTML = '<input type="checkbox" name="check">';
  cell2.innerHTML = document.getElementById('start_time').value;
  cell3.innerHTML = document.getElementById('subject').value;
  cell4.innerHTML = document.getElementById('together').value;
  cell5.innerHTML = document.getElementById('place').value;
  cell6.innerHTML = document.getElementById('no1').value;
  cell7.innerHTML = document.getElementById('no2').value;
  cell8.innerHTML = document.getElementById('distance').value;
  cell9.innerHTML = document.getElementById('no3').value;

}

/*************************************
 * 表のレコード削除
 * 説明：チェックボックスで選択された行を削除する
 * 引数：なし
 * 戻り値：なし
 *************************************/
function delTableRow() {
  $('#params tr').has('input[type=checkbox]:checked').remove();
}


// 行動履歴詳細テーブルの動作スクリプト(使用していない)
// function get_data_from_table() {
//   let data = []
//   Array.prototype.forEach.call(document.querySelectorAll("table#target>tbody>tr"), (e) => {
//       if (e.classList.contains("hide"))
//           return;
//       if (e.classList.contains("add_row"))
//           return;

//       let row = []
//       Array.prototype.forEach.call(e.querySelectorAll("td>input"), (txt) => {
//           row.push(txt.value);
//       })
//       data.push(row);
//   })
//   return data;
// }