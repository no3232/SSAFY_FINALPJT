<template>
  <div>
    <MainPageLogSign />
    <div id="rssBlock" >
          <p class="cnnContents">
            <span class="marqueeStyle">404 에러입니다.... 페이지가 없어용...(  ´・^・`) 404 에러입니다.... 페이지가 없어용...(  ´・^・`) 404 에러입니다.... 페이지가 없어용...(  ´・^・`)</span>
            <span class="marqueeStyle2">404 에러입니다.... 페이지가 없어용...(  ´・^・`) 404 에러입니다.... 페이지가 없어용...(  ´・^・`) 404 에러입니다.... 페이지가 없어용...(  ´・^・`)</span>
          </p>
        </div>
  </div>
</template>

<script>
import MainPageLogSign from '@/components/MainPageLogSign'
export default {
    name: 'MyTest',
    components: {
      MainPageLogSign
    }
    
}
</script>

<style>
  #rssBlock{
    left:0px;
    background: yellow;
    position: absolute;
    top: 50vh;
    width:100%;
    overflow: hidden;
    z-index: 10;
  }

  .cnnContents {
    width:100%;
    padding-top: 20px;
    margin:0 auto;
    font-size: 50px;
    white-space: nowrap;
    text-transform: uppercase;
    font-weight: 900;
    color: red;
  }
  .marqueeStyle {
    display:inline-block;
    animation: scrolling-left1 20s linear infinite;
  }

  .marqueeStyle2 {
    display:inline-block;
    animation: scrolling-left2 20s linear infinite;
    animation-delay: 10s;
  }

  @keyframes scrolling-left1 {
      0% {transform: translateX(100%);
          -webkit-transform: translateX(100%);}
        100% {transform: translateX(-100%);
            -webkit-transform: translateX(-100%);}
  }
  @keyframes scrolling-left2 {
      0% {transform: translateX(0%);
          -webkit-transform: translateX(0%);}
        100% {transform: translateX(-200%);
            -webkit-transform: translateX(-200%);}
  }
  
</style>