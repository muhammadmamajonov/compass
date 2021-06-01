$(document).on('change', '#gr_talabalari', function() {
    var sel = document.getElementById('gr_talabalari');
    console.log("Fan", sel);
    var gr_id = sel.options[sel.selectedIndex].value;
    console.log(gr_id)

    $.ajax({
        type: 'GET',
        url: "/dashboard/guruh-talabalari/",
        data: { i: gr_id },
        success: function(data) {
            var datas = data['data']
            var gt = ''

                for (var dt of datas) {
                    ism = dt.ism
                    id = dt.id
                    tolov = dt.tolov
                    tel = dt.tel
                    manzil = dt.manzil
                    if(tolov == 1) {
                        gt += `<tr>
                                <td>` + ism + `</td>
                                <td>` + tel + `</td>
                                <td>` + manzil + `</td>
                                <td style="color: green;">Tolov qilingan</td>
                                </tr>`
                    }
                    else{
                        gt += `<tr>
                                <td>` + ism + `</td>
                                <td>` + tel + `</td>
                                <td>` + manzil + `</td>
                                <td style="color: red;">Tolov qilinmagan</td>
                                </tr>`
                    }
                }
                document.getElementById("gr_talabalar").innerHTML = gt
        }

    })
})