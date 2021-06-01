$(document).on('change', '#guruh', function() {
    var sel = document.getElementById('guruh');

    var grid = sel.options[sel.selectedIndex].value;
    console.log("djskflljkfdslfsdl lsdjsdfjsdlkjl jlk")

    $.ajax({
        type: 'GET',
        url: "/dashboard/guruh-talabalari/",
        data: { grid: grid },
        success: function(data) {
            var datas = data['data']
            var gt
            if (grid.length > 0) {
                for (var dt of datas) {
                    ism = dt.ism
                    id = dt.t_id
                    console.log(id)
                    gt += `<option value="` + id + `">` + ism + `</option>`

                }
                document.getElementById("guruh_talabalari").innerHTML = gt

            } else {
                console.log("grid 0 dan kichik")

            }

        }

    })
})