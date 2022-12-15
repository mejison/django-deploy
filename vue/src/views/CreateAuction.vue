<template>
    <div class="column is-12 box">
                <h2 class="subtitle">Create Auction</h2>

                <p class="has-text-grey mb-4">* All fields are required</p>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>Product Name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Slug*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="slug">
                            </div>
                        </div>

                        <div class="field">
                            <label>Description*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="description">
                            </div>
                        </div>

                         <div class="field">
                            <label>Image*</label>
                            <div class="control">
                                <input type="file" class="input" id="image_file">
                            </div>
                        </div>


                        <div class="field">
                            <label>Price*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="price">
                            </div>
                        </div>
                    </div>

                    <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="column is-6">

                        <div class="field">
                            <label>Place*</label>
                            <div class="control">
                                <input type="datetime-local" class="input" v-model="date">
                            </div>
                        </div>


                    <button class="button is-dark" @click="submitForm">Submit</button>
                    </div>
                </div>
            </div>

</template>

<script>
import axios from 'axios'

export default {
    name: 'CreateAuction',
    data() {
        return {
            name: '',
            slug: '',
            description: '',
            price: '',
            image: '',
            date: '',
            errors: []
           
        }
    },
    mounted() {

    },
    methods: {

        submitForm() {
            this.errors = []

            if(this.name === ''){
                this.error.push('the name of the product is missing')
            }

            if(this.slug === ''){
                this.errors.push('the slug is missing')
            }

            if(this.description === ''){
                this.errors.push('the description is missing')
            }

            if(this.price === ''){
                this.errors.push('the price is missing')
            }

            if(this.date === ''){
                this.errors.push('the date is missing')
            }

            if(!this.errors.length){
                this.$store.commit('setIsLoading', true)
                this.DataHandler()

            }
        },

        async DataHandler() {
            const data = {
                'name': this.name,
                'slug': this.slug,
                'description': this.description,
                'price': this.price,
                'end_date': this.date,
                'image': this.image
            }

            await axios
                .post('/api/v1/create-auction/', data)
                .then(response => {
                    this.$router.push('/')
                })
                .catch(error => {
                    console.log(error)
                })
        }

    }

}

</script>