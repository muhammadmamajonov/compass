const staff = document.querySelector("#staff")
const staff1 = document.querySelector("#staff1")
    // staff1.style.display = "none"
$(document).on('keyup', function() {

    var q = document.getElementById("oqituvchi_qidiruv").value;
    console.log(q)

    $.ajax({

        type: 'get',
        url: "/dashboard/oqituvchi-qidiruv/",
        data: { q: q },

        success: function(data) {
            console.log(data)

            var datas = data['data']
            var tr
            if (q.length > 0) {
                for (var dt of datas) {
                    ism = dt.ism
                    familya = dt.familya
                    rasmUrl = dt.rasm
                    telefon = dt.tel
                    fani = dt.fan
                    guruhSoni = dt.guruh_soni
                    console.log(q)
                    console.log(familya)
                    tr += `<tr class="selected">
                   

                    <td style="width: 10px;">

                        <div class="media align-items-center">
                            <div class="avatar avatar-xs mr-2">
                                <img src="` + rasmUrl + `" alt="Avatar" class="avatar-img rounded-circle">
                            </div>
                            <div class="media-body">

                                <span class="js-lists-values-employee-name">` + ism + ` ` + familya + `</span>

                            </div>
                        </div>

                    </td>
                    <td>

                        <div class="media align-items-center">

                            <div class="media-body">

                                <span class="js-lists-values-employee-name">` + telefon + `</span>

                            </div>
                        </div>

                    </td>

                    <td>
                        <div class="media align-items-center">
                            <a>` + fani + `</a>
                           
                        </div>
                    </td>

                    <td>` + guruhSoni + `</td>

                </tr>`
                }
                document.getElementById("staff1").innerHTML = tr
                staff.style.display = 'none'
                staff1.style.display = ""
            } else {
                staff1.style.display = "none"
                staff.style.display = ""
            }

        }




    })
})

// const oqituvchi_qidiruv = document.querySelector("#oqituvchi_qidiruv")
// const tableOutput - document.querySelector('.table-output')
// tableOutput.style.display = 'none';

// oqituvchi_qidiruv.addEventListener("keyup", (e) =>{
//     const searchValue = e.target.value;

//     if (searchValue > 0){
//         console.log('searchValue', searchValue)

//         fetch("/dashboard/oqituvchi-qidiruv/",{
//             body: JSON.stringify({searchText: searchValue})
//             method: "POST",

//         }) 
//         .then((res) => res.json())
//         .then((data) => {
//             console.log("data": data)
//             tableOutput.style.display = "block";
//         });
//     }
//     else{
//         console.log("hato")
//     }
// });