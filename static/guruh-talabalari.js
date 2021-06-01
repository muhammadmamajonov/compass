var i

function guruhtalaba(id) {
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
            console.log(datas)

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
                    ` 
                    <tr>
                        <td>` + i + `</td>
                        <td> <button type="button" class="btn btn-link"  data-toggle="modal" data-target="#oquvchi_davomatModal` + id + `">` + ism + `</button></td>
                        <td>` + guruh + `</td>
                        <td>` + tel + `</td>
                        <td><input class="ml-2" type="checkbox" name="bor-yoq" value="` + id + `"></td>
                    </tr>`;
            }

            gt += `<tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td> <input class="btn btn-outline-primary" type="submit" value="davomat" ></td>
                    <input type='hidden' name="gur_id" value="` + guruh_id + `"
                    </tr>
                   
                    `;
            console.log(gt)
            document.getElementById("guruh_talabalar").innerHTML = gt;
        }
    })
}