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
          ></v-data-table>
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
export default {
  data() {
    return {
      leaderboardData: [
        { id: 1, name: "Hacker A", points: 100 },
        { id: 2, name: "Hacker B", points: 85 },
        { id: 3, name: "Hacker C", points: 75 },
        { id: 3, name: "Hacker C", points: 75 },
        { id: 3, name: "Hacker C", points: 75 },
        { id: 3, name: "Hacker C", points: 75 },
        { id: 3, name: "Hacker C", points: 75 },
        { id: 3, name: "Hacker C", points: 75 },
        { id: 3, name: "Hacker C", points: 75 },
        { id: 3, name: "Hacker C", points: 75 },
        // Add more leaderboard data here
      ],
      tableHeaders: [
        { text: "S.No", value: "id" },
        { text: "Name of Hackers", value: "name" },
        { text: "Points", value: "points" },
      ],
    };
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
