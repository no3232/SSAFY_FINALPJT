<template>
<div class="d-flex container-fluid">
  <div class="d-flex viewport overflow-hidden " ref="viewport">
    <div class="d-flex row flex-nowrap " id="horizontalScroll" ref="content">
        <FirstSelectCard 
            v-for="movie in selected"
            :key="movie.title"
            :movie="movie"
            @movieId="movieId"
        />
    </div>
    <i class="bi bi-chevron-left fs-1" @click.stop="clickLeft"></i>
    <i class="bi bi-chevron-right fs-1" @click.stop="clickRight"></i>
  </div>
</div>
</template>

<script>
import ScrollBooster from 'scrollbooster'
import FirstSelectCard from '@/components/FirstSign/FirstSelectCard'

export default {
    name: 'FirstSelectScroll',
    components: {
        FirstSelectCard,
    },
    props: {
        selected: Array,
    },
    data() {
        return {
            scrollB: null,
        }
    },
    computed: {
    },
    methods: {
        // 스크롤 부스터
        sb() {
            // refs를 통해서 html요소 정보를 불러올 수 있습니다.
            const viewport = this.$refs.viewport
            const content = this.$refs.content
            // eslint-disable-next-line
            // 리턴으로 스크롤 부스터 객체를 반환
            return new ScrollBooster({
                viewport,
                content,
                direction: "horizontal",
                scrollMode: "transform",
            })
        },
        clickLeft() {
            // 현재 포지션을 받아옴
            const xPosition = this.scrollB.getState().position.x
            // xPosition+this.scrollB.edgeX.from: 스크롤 할 컨텐츠의 전체 넓이
            if (xPosition>-10) {this.scrollB.scrollTo({ x: xPosition+this.scrollB.edgeX.from/5 , y: 0})
                setTimeout(()=>{
                if (this.scrollB.getState().position.x < 0) {
                    this.scrollB.scrollTo({ x: 0 , y: 0})
                }}, 250)
            }
        },
        clickRight() {
            console.log(this.scrollWidth)
            const xPosition = this.scrollB.getState().position.x
            if (xPosition< -this.scrollB.edgeX.from + 10) {
                this.scrollB.scrollTo({ x: xPosition-this.scrollB.edgeX.from/5 , y: 0})
                setTimeout(()=>{
                if (this.scrollB.getState().position.x > -this.scrollB.edgeX.from) {
                    this.scrollB.scrollTo({ x: -this.scrollB.edgeX.from , y: 0})
                }}, 250)
            }
        },
        movieId(movie) {
            this.$emit('movieId', movie)
        }
    },
    mounted() {
        // 마운트 될 때 스크롤 함수 동작하게 설정
        // eslint-disable-next-line
        this.scrollB = this.sb()
    }
}
</script>

<style>
.viewport {
    position: relative;
}
.bi-chevron-left {
    background-color: white;
    opacity: 0.5;
    border-radius: 10%;
    position: absolute;
    top: 43%;
    left: 10px;
}
.bi-chevron-right {
    background-color: white;
    opacity: 0.5;
    border-radius: 10%;
    position: absolute;
    top: 43%;
    right: 10px;
}
#horizontalScroll {
  width: 100vw;
}
</style>