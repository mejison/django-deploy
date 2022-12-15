<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="product.get_image">
                </figure>

                <h1 class="title">{{ product.name }}</h1>

                <p>{{ product.description }}</p>
            </div>

            <div class="column is-3">
                <h2 class="subtitle">Information</h2>

                <p><strong>Price: </strong>${{ product.price}}</p>

                <div class="field has-addons mt-6">
                    <div class="field">
                        <div class="control">
                           <input type="number" class="input" v-model="bid">
                        </div>
                    </div>

                    <div class="control">
                        <button class="button is-dark" @click="submitForm">Submit</button>
                    </div>
                </div>

                <div v-if="product.bid_active === true">
                            <label>Ask Question</label>
                            <div class="control">
                                <input type="text" class="input" v-model="ques">
                            </div>
                            <div class="control">
                            <button class="button is-dark" @click="submitQuestion">Ask</button>
                            </div>
                </div>
                <div v-else>
                <h1><b> BIDDING ENDED! </b></h1>
                 <div class="control">
                        <button class="button is-dark" @click="submitmail">SEND MAIL TO THE WINNER</button>
                    </div>
                </div>
                <div
                 class="column is-3"
                 v-for="ans in answer"
                 v-bind:key="answer.id"
                 >
                 <div
                 class="column is-3"
                 v-for="q in question"
                 v-bind:key="question.id"
                 >
                <div>
                <p>question: {{ q.question_text }}</p>
                <p>answer: {{ ans.answer }}</p>
                </div>
                </div>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {

    name: 'Product',
    props: {
    product: Object,
    question: Object
    },
    data() {
        return {
            product: {},
            bidactive: '',
            question: [],
            answer: [],
            bid: '',
            ques: '',
            errors: []
        }
    },
    mounted() {
        this.getProduct(),
        this.getQuestion(),
        this.getAnswer()
    },
    methods: {

        async getAnswer() {

            this.$store.commit('setIsLoading', true)
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/getanswer/${product_slug}`)
                .then(response => {
                    this.answer = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)

        },



        async getProduct() {

            this.$store.commit('setIsLoading', true)
            const product_slug = this.$route.params.product_slug
            await axios
                .get(`/api/v1/products/${product_slug}`)
                .then(response => {
                    this.product = response.data
                    
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)
        },
        async getQuestion() {
            this.$store.commit('setIsLoading', true)

            const product_slug = this.$route.params.product_slug
            
            await axios
                .get(`/api/v1/getquestion/${product_slug}`)
                .then(response => {
                    this.question = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)
        },

        submitForm(){
             this.errors = []

             if(this.bid === ''){
                this.errors.push('the bid is missing')
             }

             if(!this.errors.length){
                this.$store.commit('setIsLoading', true)
                this.AuctionHandler()
             }

        },

        async AuctionHandler(){
            const data = {
                'bid': this.bid
            }
            await axios
                .post('/api/v1/bid/', data)
                .then(response => {
                    this.$router.push('/')
                })
                .catch(error => {
                    console.log(error)
                })
        },

        submitQuestion() {
            this.$store.commit('setIsLoading', true)
            this.QuestionHandler()
        },
        async QuestionHandler(){
            const data = {
                'question_text': this.ques
            }
            await axios
                .post('/api/v1/question/', data)
                .then(response => {
                    this.$router.push('/')
                })
                .catch(error => {
                    console.log(error)
                })
        },

        submitmail() {
            this.mailHandler()
        },

        async mailHandler() {
            this.$store.commit('setIsLoading', true)
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/sendmail/${product_slug}/`)
                .then(response => {
                    
                })
                .catch(error => {
                    console.log(error)
                })

             this.$store.commit('setIsLoading', false)
        }
    }
}
</script>