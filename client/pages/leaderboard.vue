<template>
  <v-container>
    <v-toolbar-title>Leaderboard</v-toolbar-title>
    <v-divider></v-divider>
    <v-layout class="mt-4">
      <v-flex xs8>
        <v-card class="leaderboard">
  <v-card-title>Leaderboard Table</v-card-title>
  <v-divider></v-divider>
  <v-data-table
    :headers="tableHeaders"
    :items="leaderboardData"
    :items-per-page="10"
    class="elevation-1 table-wrapper"
  >
    <template v-slot:item.name="{ item }">
      <td>{{ item.user }}</td>
    </template>
    <template v-slot:item.score="{ item }">
      <td>{{ item.score }}</td>
    </template>
  </v-data-table>
</v-card>
      </v-flex>
      <v-flex xs4 class="ml-4">
        <v-card>
          <v-card-text class="justify-space-between">
            <h3>Data Card 1</h3>
            <p>Sample data 1</p>
          </v-card-text>
        </v-card>
        <v-card class="mt-4">
          <v-card-text class="justify-space-between">
            <h3>Data Card 1</h3>
            <p>Sample data 1</p>
          </v-card-text>
        </v-card>
        <v-card class="mt-4">
          <v-card-text class="justify-space-between">
            <h3>Data Card 1</h3>
            <p>Sample data 1</p>
          </v-card-text>
        </v-card>
        <v-card class="mt-4">
          <v-card-text class="justify-space-between">
            <h3>Data Card 1</h3>
            <p>Sample data 1</p>
          </v-card-text>
        </v-card>
        <v-card class="mt-4">
          <v-card-text class="justify-space-between">
            <h3>Data Card 1</h3>
            <p>Sample data 1</p>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-row class="mt-4">
      <v-col>
        <v-card>
          <v-card-text class="justify-space-between">
            <h3>Data Card 1</h3>
            <p>Sample data 1</p>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col>
        <v-card>
          <v-card-text class="justify-space-between">
            <h3>Data Card 1</h3>
            <p>Sample data 1</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      leaderboardData: [],
      tableHeaders: [
        { text: "S.No", value: "id" },
        { text: "Name of Hackers", value: "name" },
        { text: "Score", value: "score" },
      ],
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/company/dashboard/"
        );
        this.leaderboardData = response.data.Leaderbooard;
        console.log(response.data.Leaderbooard);
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
.v-card,
.v-data-table {
  background-color: #0f1724 !important;
}
/*  */
.table-wrapper {
  height: 350px; /* Fill the available height within the card */
  overflow-y: auto; /* Add a scrollbar when there are more than 10 entries */
}
</style>
