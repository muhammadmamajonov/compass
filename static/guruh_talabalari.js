

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
                var t;
                t = 0
                for (var dt of datas) {
                    ism = dt.ism;
                    id = dt.id;
                    guruh = dt.guruh;
                    tel = dt.tel;
                    tolov = dt.tolov;
                    manzil = dt.manzil;
                    taklif = dt.taklif;
                    taklif_qilgan = dt.taklif_qilganlari;
                    qayerdan_keldi = dt.qayerdan_keldi;
                    filyal = dt.filyal;

                    if (tolov == 1) {
                        t += 1
                        gt +=
                            `<tr>
                                <td>` + t + `</td>
                                <td><a href="/dashboard/talaba` + id  +`" style="background-color: white; border: none; outline: none;" >` + ism + `</a></td>
                                <td>` + guruh + `</td>
                                    <td style="color: green">Qilingan </td>
                                <td>` + tel + `</td>

                                <td>` + manzil + `</td>
                                <td>` + qayerdan_keldi + `</td>
                                <td style="text-align: center;">` + taklif + `</td>
                                <td style="text-align: center;">` + taklif_qilgan + `</td>
                                <td>` + filyal + `</td>
                            </tr>`
                    } else {
                        t += 1
                        gt +=
                            `<tr>
                                <td>` + t + `</td>
                                <td><a href="/dashboard/talaba/` + id +`" style="background-color: white; border: none; outline: none;" >` + ism + `</a></td>
                                <td>` + guruh + `</td>
                                    <td style="color: red">Qilinmagan </td>
                                <td>` + tel + `</td>
                                <td>` + manzil + `</td>
                                <td>` + qayerdan_keldi + `</td>
                                <td style="text-align: center;">` + taklif + `</td>
                                 <td style="text-align: center;">` + taklif_qilgan + `</td>
                                 <td>` + filyal + `</td>
                            </tr>`

                    }


                }

                document.getElementById("gurtalabalar").innerHTML = gt;


            }

        })
    }
