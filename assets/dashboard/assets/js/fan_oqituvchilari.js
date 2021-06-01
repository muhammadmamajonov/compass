$(document).on('change', '#fan', function() {
    var sel = document.getElementById('fan');

    var fan_id = sel.options[sel.selectedIndex].value;
    console.log(fan_id)

    $.ajax({
        type: 'GET',
        url: "/dashboard/fan-oqituvchilari/",
        data: { fan_id: fan_id },
        success: function(data) {
            var datas = data['data']
            var oq
            if (fan_id.length > 0) {
                for (var dt of datas) {
                    idsi = dt.id
                    ism = dt.ism
                    fam = dt.fam
                    console.log(ism)
                    oq += `<option value="` + idsi + `">` + ism + ` ` + fam + `</option>`

                }
                document.getElementById("oqituvchi").innerHTML = oq

            } else {
                console.log("grid 0 dan kichik")

            }

        }

    })
})