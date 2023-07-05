<template>
  <v-container>
    <!-- Overview Card Row -->
    <v-layout row class="mb-4 mt-4">
      <v-flex xs4>
        <v-card class="overview-card">
          <v-card-title class="justify-start">Overview</v-card-title>
          <v-card-text>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec fringilla mauris.
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card class="rewards-card ml-4">
          <v-card-title class="justify-start">Rewards</v-card-title>
          <v-card-text>
            Total amount distributed this week: $10,000
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card class="active-hackathons-card ml-4">
          <v-card-title class="justify-start">Registered Users</v-card-title>
          <v-card-text>
            Total registered users: 500
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>

    <!-- Participants, Leaderboard, and Registered Users Row -->
    <v-layout row>
      <v-flex xs8>
        <v-card >
          <v-card-text class="d-flex combined-card">
            <v-card class="participants-card">
              <v-card-title class="justify-start">Participants</v-card-title>
              <v-card-text>
                <v-progress-circular
                  :size="100"
                  :width="10"
                  :value="75"
                  color="primary"
                ></v-progress-circular>
                <p>Total participants: 75</p>
              </v-card-text>
            </v-card>

            <v-card class="leaderboard-card">
              <v-card-title>Leaderboard</v-card-title>
              <v-divider></v-divider>
              <v-list>
                <v-list-item v-for="entry in leaderboardEntries" :key="entry.id">
                  <v-list-item-title>{{ entry.name }}</v-list-item-title>
                  <v-list-item-subtitle>{{ entry.points }} points</v-list-item-subtitle>
                </v-list-item>
              </v-list>
            </v-card>
          </v-card-text>
        </v-card>
      </v-flex>

      <v-flex xs4>
        <v-card class="registered-users-card ml-4">
         
          <v-card-title class="justify-start">Active Hackathons</v-card-title>
          <v-card-text>
            Number of active hackathons: 5
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      leaderboardEntries: [
        { id: 1, name: "User A", points: 100 },
        { id: 2, name: "User B", points: 85 },
        { id: 3, name: "User C", points: 75 },
        { id: 4, name: "User D", points: 65 },
        { id: 5, name: "User E", points: 50 },
      ],
    };
  },
};
</script>

<style scoped>
.overview-card,
.rewards-card,
.active-hackathons-card,
.participants-card,
.leaderboard-card,
.registered-users-card {
  margin-bottom: 16px;
}

.participants-card,
.leaderboard-card {
  width: calc(50% - 8px);
  height: 300px;
}

.registered-users-card {
  width: calc(50% - 8px);
  margin-left: 8px;
}

.overview-card,
.rewards-card,
.active-hackathons-card {
  height: 200px;
}
.combined-card {
  display: flex;
  width: 100%;
  justify-content: space-between;
}

.registered-users-card,
.participants-card {
  margin-right: 8px;
}

.leaderboard-card {
  overflow-y: auto;
  max-height: 300px;
  width: 48%;
  margin-left: 10px;
}
.participants-card {
  width: 48%;
  margin-right: 10px; 
}
.registered-users-card {
  width: 96%;
  
}
</style>
