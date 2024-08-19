$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString()
    // console.log(id)
    var ele=this.parentNode.children[2]
    var par=this.parentNode.parentNode.children[3].children[1].children[0].children[0]
    // console.log(par.innerText)
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success:function(data){
            ele.innerText=data.quantity
            const pri=document.getElementById('total_price');
            pri.innerText=`₹ ${data.price}`
            const final=document.getElementById('final_price');
            final.innerText=`₹ ${data.total}`
            const discount=document.getElementById('discount_price');
            discount.innerText=`-₹ ${data.discount}`
            const disc=document.getElementById('final-discount');
            disc.innerText=`You will save ₹ ${data.discount} on this order`;
            var cost=par.innerText;
            console.log(cost);
            par.innerText=parseInt(par.innerText)+(cost/parseInt(data.quantity-1))
        }
    })
})



$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString()
    // console.log(id)
    var ele=this.parentNode.children[2]
    var par=this.parentNode.parentNode.children[3].children[1].children[0].children[0]
    // console.log(this.parentNode.children[4])
    // console.log(this.parentNode.children[2].innerText)
    qty=this.parentNode.children[2].innerText;
    if(qty==1){
        $('#minimum').removeClass('d-none');
        setTimeout((()=>{
            $('#minimum').addClass('d-none');
        }),3000)
    }
else{
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id
        },
        success:function(data){
            ele.innerText=data.quantity
            const pri=document.getElementById('total_price');
            pri.innerText=`₹ ${data.price}`
            const final=document.getElementById('final_price');
            final.innerText=`₹ ${data.total}`
            const discount=document.getElementById('discount_price');
            discount.innerText=`-₹ ${data.discount}`
            const disc=document.getElementById('final-discount');
            disc.innerText=`You will save ₹ ${data.discount} on this order`;
            var cost=par.innerText;
            // console.log(cost);
            par.innerText=parseInt(par.innerText)-(cost/parseInt(data.quantity+1))
        }
    })
}
})




// $('.remove-item').click(function(){
//     var id=$(this).attr("pid").toString()
//     // console.log(id)
//     // var ele=this.parentNode.children[0]
//     // var par=this.parentNode.parentNode.children[3].children[1].children[0].children[0]
//     // console.log(id)
//     // console.log(this.parentNode.children)
//     $.ajax({
//         type:"GET",
//         url:"/removecart",
//         data:{
//             prod_id:id
//         },
//         success:function(data){
//             redirect("cart")
//         }
//     })
// })

$('.add-to-cart').click(function(){
  $('#addtocart').removeClass('d-none');
  setTimeout(()=>{
    $('#addtocart').addClass('d-none');
  },3000)
})
