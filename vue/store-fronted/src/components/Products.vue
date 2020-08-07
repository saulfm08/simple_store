<template>
<main role="main">
        <section class="jumbotron text-center">
        <div class="container">
          <h1>Ofertas Imperdíveis</h1>
          <p class="lead text-muted">As melhores ofertas com os melhores preços!</p>
          <!--p>
            <a href="#" class="btn btn-primary my-2">Main call to action</a>
            <a href="#" class="btn btn-secondary my-2">Secondary action</a>
          </p-->
        </div>
      </section>    
      <div class="album py-5 bg-dark">

    <b-container class="bv-example-row">
        <b-row v-for="chunk in productChunks" v-bind:key="chunk.id">
            <b-col :product="sp" v-for="sp in chunk" v-bind:key="sp.id">
                <b-card
                    :title=sp.name
                    img-src="https://picsum.photos/600/300/?image=25"
                    img-alt="Image"
                    img-top
                    tag="article"
                    style="max-width: 20rem;"
                    class="mb-2">
                    <b-card-text>
                    Some quick example text to build on the card title and make up the bulk of the card's content.
                    </b-card-text>

                    <b-button :href=sp.id variant="secondary">Detalhes</b-button> <span></span>
                    <b-button :href=sp.url variant="primary">Compre já!</b-button>
                </b-card>
            </b-col>
        </b-row>          
    </b-container>
      </div>
</main>
</template>


<script>
import axios from 'axios'
import lodash from 'lodash';

export default {
    name: "ProductList",
    ProductThumbnail: true,
    data() {
        return {
            products: [],
            itemsPerRow: 3
        }
    },
    async mounted () {
        await axios.get('http://127.0.0.1/api/product/?format=json')
        .then(
        response => {
            this.products = response.data
            console.log('line 42', response.data)
        })
        .catch(function (error) {
        this.errors.push(error)
        console.log('line 46', error)
        })
    },
    computed: {
        productChunks() {
            return lodash.chunk(Object.values(this.products), this.itemsPerRow);
        }
    }
}
</script>