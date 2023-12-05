function _class(name){
  return document.getElementsByClassName(name);
}

let tabPanes = document.querySelectorAll('.tab-header-item')
console.log(tabPanes)

for(let i=0;i<tabPanes.length;i++){
  tabPanes[i].addEventListener("click",function(){
  document.getElementsByClassName("tab-header-item active")[0].classList.remove("active");
    _class("tab-header-item")[i].classList.add("active");
    document.getElementsByClassName("tab-content-item active")[0].classList.remove("active");
    _class("tab-content-item")[i].classList.add("active");
  });
}