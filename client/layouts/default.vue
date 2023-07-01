<template>
  <v-app dark>
    <v-main>
      <Navbar/>
      <Sidebar/>
      <Nuxt />
    </v-main>
  </v-app>
</template>
<style>
.navbar {
  display: flex !important;
  justify-content: space-around !important;
  align-items: baseline;
  position: relative;
}
.cards {
  margin-top: 40px;
  margin-left: 6rem;
}
.v-card {
  background-color: #0f1724;
}
.row {
  justify-content: center;
}
.v-dialog {
  overflow: hidden !important;
}
.v-card__title {
  justify-content: center;
}
.v-card__text {
  display: flex;
}
.v-card__actions {
  align-items: center;
  justify-content: center;
}
.searchbar {
  display: flex;
  align-items: center;
  width: 300px;
  margin-left: 100px;
}
.v-input__control {
  height: 55px;
}
.search-field {
  width: 100%;
  background-color: grey;
}

.icons {
  margin-left: auto;
}

.sidebar {
  width: 70px !important;
}
.v-main {
  padding: 0 !important;
}
.search-bar {
  margin-right: auto;
  margin-left: 20px;
}

.v-icon {
  font-size: 34px !important;
}
.v-icon:hover {
  cursor: pointer;
}

.v-navigation-drawer__content {
  overflow: hidden !important;
}
.toolbar__content > *:not(:first-child):not(:last-child) {
  margin-left: 8px;
}
.v-text-field {
  width: 200px;
  height: 55px;
}
.toolbar__content {
  display: flex;
  align-items: center;
}
.container {
  /* display: flex;
      justify-content: center; */
  text-align: center !important;
}
</style>
