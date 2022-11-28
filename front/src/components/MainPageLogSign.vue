<template>
  <div v-show="!$store.getters.userPkGetters" style="color: white;">
    <div class="login" ref="login" @mouseover="moving" @mouseleave="unmoving" @click="gotoLogin">
        <div id="firstLogin">
            <div id="L" ref="L">L</div>
            <div id="O" ref="O">O</div>
            <div id="G" ref="G">G</div>
            <div id="I" ref="I">I</div>
            <div id="N" ref="N">N</div>
        </div>
        <div id="SecondLogin">
            <div id="L2" ref="L2">L</div>
            <div id="O2" ref="O2">O</div>
            <div id="G2" ref="G2">G</div>
            <div id="I2" ref="I2">I</div>
            <div id="N2" ref="N2">N</div>
        </div>
    </div>
    <div class="signup" ref="signup" @mouseover="signmoving" @mouseleave="signunmoving" @click="gotoSignup">
        <div id="firstLogin">
            <div id="SS" ref="SS">S</div>
            <div id="SI" ref="SI">I</div>
            <div id="SG" ref="SG">G</div>
            <div id="SN" ref="SN">N</div>
            <div id="SU" ref="SU">U</div>
            <div id="SP" ref="SP">P</div>
        </div>
        <div id="SecondLogin">
            <div id="SS2" ref="SS2">S</div>
            <div id="SI2" ref="SI2">I</div>
            <div id="SG2" ref="SG2">G</div>
            <div id="SN2" ref="SN2">N</div>
            <div id="SU2" ref="SU2">U</div>
            <div id="SP2" ref="SP2">P</div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'MainPageLogSign',
    methods: {
      moving() {
        this.$refs.L.classList.add('LL')
        this.$refs.O.classList.add('LO')
        this.$refs.G.classList.add('LG')
        this.$refs.I.classList.add('LI')
        this.$refs.N.classList.add('LN')
        this.$refs.L2.classList.add('LL')
        this.$refs.O2.classList.add('LO')
        this.$refs.G2.classList.add('LG')
        this.$refs.I2.classList.add('LI')
        this.$refs.N2.classList.add('LN')
      },
      unmoving() {
        this.$refs.L.classList.remove('LL')
        this.$refs.O.classList.remove('LO')
        this.$refs.G.classList.remove('LG')
        this.$refs.I.classList.remove('LI')
        this.$refs.N.classList.remove('LN')
        this.$refs.L2.classList.remove('LL')
        this.$refs.O2.classList.remove('LO')
        this.$refs.G2.classList.remove('LG')
        this.$refs.I2.classList.remove('LI')
        this.$refs.N2.classList.remove('LN')
      },
      signmoving() {
        this.$refs.SS.classList.add('SS')
        this.$refs.SI.classList.add('SI')
        this.$refs.SG.classList.add('SG')
        this.$refs.SN.classList.add('SN')
        this.$refs.SU.classList.add('SU')
        this.$refs.SP.classList.add('SP')
        this.$refs.SS2.classList.add('SS')
        this.$refs.SI2.classList.add('SI')
        this.$refs.SG2.classList.add('SG')
        this.$refs.SN2.classList.add('SN')
        this.$refs.SU2.classList.add('SU')
        this.$refs.SP2.classList.add('SP')
      },
      signunmoving() {
        this.$refs.SS.classList.remove('SS')
        this.$refs.SI.classList.remove('SI')
        this.$refs.SG.classList.remove('SG')
        this.$refs.SN.classList.remove('SN')
        this.$refs.SU.classList.remove('SU')
        this.$refs.SP.classList.remove('SP')
        this.$refs.SS2.classList.remove('SS')
        this.$refs.SI2.classList.remove('SI')
        this.$refs.SG2.classList.remove('SG')
        this.$refs.SN2.classList.remove('SN')
        this.$refs.SU2.classList.remove('SU')
        this.$refs.SP2.classList.remove('SP')
      },
      gotoLogin() {
        this.$router.push({name:'login'})
      },
      gotoSignup() {
        this.$router.push({name:'signup'})
      }
    }
}
</script>

<style>
.login {
            display: flex;
            flex-direction: column;
            height: 140px;
            font-size: 100px;
            flex-wrap: nowrap;
            overflow: hidden;
            z-index: 100;
        }
  .signup {
            display: flex;
            flex-direction: column;
            height: 140px;
            font-size: 100px;
            flex-wrap: nowrap;
            overflow: hidden;
            z-index: 100;
        }
        #firstLogin {
            display: flex;
        }
        #SecondLogin {
            display: flex;
        }
        .LL {
            animation: topgo 2s;
            animation-fill-mode: forwards;
        }
        .LO {
            animation: topgo 2s;
            animation-delay: 0.1s;
            animation-fill-mode: forwards;
        }
        .LG {
            animation: topgo 2s;
            animation-delay: 0.2s;
            animation-fill-mode: forwards;
        }
        .LI {
            animation: topgo 2s;
            animation-delay: 0.3s;
            animation-fill-mode: forwards;
        }
        .LN {
            animation: topgo 2s;
            animation-delay: 0.4s;
            animation-fill-mode: forwards;
        }
        .SS {
            animation: topgo 2s;
            animation-fill-mode: forwards;
        }
        .SI {
            animation: topgo 2s;
            animation-delay: 0.1s;
            animation-fill-mode: forwards;
        }
        .SG {
            animation: topgo 2s;
            animation-delay: 0.2s;
            animation-fill-mode: forwards;
        }
        .SN {
            animation: topgo 2s;
            animation-delay: 0.3s;
            animation-fill-mode: forwards;
        }
        .SU {
            animation: topgo 2s;
            animation-delay: 0.4s;
            animation-fill-mode: forwards;
        }
        .SP {
            animation: topgo 2s;
            animation-delay: 0.5s;
            animation-fill-mode: forwards;
        }
        @keyframes topgo {
            0% {
                transform: translateY(0);
            }
            100% {
                transform: translateY(-140px);
                background-color: white;
                color: black;
            }
        }
</style>