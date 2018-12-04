<template>
  <div class="wrapper-column">
    <div class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-offset-2 is-8">
            <slot></slot>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Column',
}
</script>

<style scoped lang="stylus">
</style>
