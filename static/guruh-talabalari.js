var i

function guruhtalaba() {
    id = document.getElementById("guruh").value
    
    i = id
    $.ajax({
        type: 'GET',
        url: "/dashboard/guruh-talabalari/",
        data: {
            i: i
        },
        success: function(data) {
            var datas = data['data'];
            var gt = '';
            i = 0;

            for (var dt of datas) {
                ism = dt.ism;
                id = dt.id;
                guruh = dt.guruh;
                guruh_id = dt.guruh_id;
                tel = dt.tel;
                tolov = dt.tolov;
                manzil = dt.manzil;
                i = i + 1;
                gt +=
                    `<option value="" disabled selected>--Talaba--</option>
                     <option value="` + id + `">` + ism + `</option>
                    `;
            }

            document.getElementById("talaba").innerHTML = gt;
        }
    })
}