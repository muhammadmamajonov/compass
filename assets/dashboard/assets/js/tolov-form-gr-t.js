$(document).on('change', '#guruhi', function() {
    var selec = document.getElementById('guruhi');

    var gr_id = selec.options[selec.selectedIndex].value;


    $.ajax({
        type: 'GET',
        url: "/dashboard/tolov_form_grtalabalar/",
        data: { gr_id: gr_id },
        success: function(data) {
            var datas = data['data']
            var gt
            if (gr_id.length > 0) {
                for (var dt of datas) {
                    ism = dt.ism
                    id = dt.t_id
                    console.log(id)
                    gt += `<option value="` + id + `">` + ism + `</option>`

                }
                document.getElementById("gr_t").innerHTML = gt

            } else {
                console.log("grid 0 dan kichik")

            }

        }

    })
})