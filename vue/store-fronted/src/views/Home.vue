<template>
<main role="main">
        <section class="jumbotron text-center">
        <div class="container">
          <h1>Album example</h1>
          <p class="lead text-muted">Something short and leading about the collection </p>
          <p>
            <a href="#" class="btn btn-primary my-2">Main call to action</a>
            <a href="#" class="btn btn-secondary my-2">Secondary action</a>
          </p>
        </div>
      </section>    
      <div class="album py-5 bg-dark">
      </div>
</main>
</template>
<script>
// @ is an alias to /src
import Products from '@/components/Products.vue'

export default {
  name: 'Home',
  components: {
    Products
  }
}
</script>
