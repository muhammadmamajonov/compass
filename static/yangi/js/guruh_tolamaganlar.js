$(".submit").click(function() {
        var ids = $(this).closest(".container").find('.ids').val();
        var txtname = $(this).closest(".container").find('.productname').text();

        console.log(ids, " ldf")
        $.ajax({

            type: 'get',
            url: "/dashboard",
            data: {ids: ids},

            success: function (data) {
                console.log(data)

                var datas = data['data']
                var tr
                if (q.length > 0) {
                    for (var dt of datas) {

                    }
                }
            }
        });
    })