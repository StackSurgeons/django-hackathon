<template>
  <v-container>
    <!-- Overview Card Row -->
    <v-layout row class="mb-4 mt-4">
      <v-flex xs4>
        <v-card class="overview-card">
          <v-card-title class="justify-start">Past Hackathons</v-card-title>
          <v-divider></v-divider>
          <v-card-text class="past-hackathons">
            <v-row class="active-hackathons ">
              <v-col v-for="past in pasthackathons" :key="past.id" cols="12">
                <v-card>
                  <v-card-text class="justify-space-between">
                    <p>{{ past.name }}</p>
                    <p>{{ past.end_date }}</p>
                    <!-- <p>Rewards: {{ past.rewards }}</p> -->
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card class="rewards-card ml-4">
          <v-card-title class="justify-start">Rewards</v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            Total amount distributed this week:
            <v-card-subtitle style="font-size: 36px;">
              $ {{ getTotalAmount() }}
            </v-card-subtitle>
            
          </v-card-text>
          <v-card-actions>
            <v-btn outlined color="primary" to="/payrewards">Pay</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card class="active-hackathons-card ml-4">
          <v-card-title class="justify-start">Registered Users</v-card-title>
          <v-divider></v-divider>
          <v-row>
            <v-col>
              <v-card v-for="(user, index) in visibleUsers" :key="index" class="user-card" cols="6" sm="4" md="3">
                <v-card-text class="mb-2 pa-0">
                  <p class="mb-0">{{ index + 1 }}: {{ user.user }}</p>
                </v-card-text>
              </v-card>
              <v-card v-if="showMore" @click="showMoreCards">
                <v-card-text>
                  <p>Show More</p>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-card>
      </v-flex>
    </v-layout>

    <!-- Participants, Leaderboard, and Registered Users Row -->
    <v-layout row>
      <v-flex xs8>
        <v-card>
          <v-card-text class="d-flex combined-card">
            <v-card class="participants-card">
              <v-card-title class="justify-start">Participants</v-card-title>
              <v-card-text>
                <v-progress-circular :size="100" :width="10" :value="75" color="primary"></v-progress-circular>
                <p>Total participants: 75</p>
              </v-card-text>
            </v-card>
            <v-card class="leaderboard-card">
              <v-card-title class="title">Leaderboard</v-card-title>
              <v-divider></v-divider>
              <v-list class="leaderboard-list">
                <v-list-item v-for="team in leaderboard" :key="team.id">
                  <v-list-item-content class="team-info">
                    <div :class="{
                      'team-header': true,
                      highlighted: team.highlighted,
                    }">
                      <p class="team-name">{{ team.team }}</p>
                      <p class="team-points">{{ team.score }} points</p>
                    </div>
                    <div class="team-members">
                      <ul class="team-members-list">
                        <li v-for="member in team.membersname" :key="member">
                          {{ member }}
                        </li>
                      </ul>
                    </div>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card class="registered-users-card ml-4">
          <v-card-title class="justify-start">Active Hackathons <v-btn to="/companyform" outlined>Start</v-btn></v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-row class="active-hackathons">
              <v-col v-for="active in activehackathons" :key="active.id" cols="12">
                <v-card>
                  <v-card-text class="justify-space-between">
                    <p>{{ active.name }}</p>
                    <p>{{ active.end_date }}</p>
                    <p>Rewards: {{ active.rewards }}</p>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      activeUsers: [],
      activehackathons: [],
      pasthackathons: [],
      leaderboard: [],
      rewards: [],
      visibleUsers: [],
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
        this.activeUsers = response.data.active_user;
        this.pasthackathons = response.data.past_hackathons;
        this.activehackathons = response.data.active_hackathons;
        this.leaderboard = response.data.Leaderbooard;
        this.rewards = response.data.reward;
        console.log(response.data.Leaderbooard);

      } catch (error) {
        console.error(error);
      }
    },
    getTotalAmount() {
      let total = 0;
      for (const reward of this.rewards) {
        total += reward.amt;
      }
      return total;
    },
    showMoreCards() {
      this.showMore = false;
      this.visibleUsers = this.activeUsers;
    },
  },
  watch: {
    activeUsers(newVal) {
      if (newVal.length <= 2) {
        this.visibleUsers = newVal;
      } else {
        this.visibleUsers = newVal.slice(0, 2);
        this.showMore = true;
      }
    },
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

.title {
  position: sticky;
  top: 0;
  padding: 16px;
  font-size: 20px;
  font-weight: bold;
}

.leaderboard-list {
  overflow-y: auto;
  max-height: 200px;
}

.active-hackathons {
  max-height: 250px;
  overflow-y: auto;
  overflow-x: hidden;
  margin-top: 16px;
}

.past-hackathons {
  height: 120px !important;
}

.active-hackathons::-webkit-scrollbar {
  width: 8px;
}

.active-hackathons::-webkit-scrollbar-track {
  background: #f1f1f1;
}

.active-hackathons::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 4px;
}

.active-hackathons::-webkit-scrollbar-thumb:hover {
  background: #555;
}

.leaderboard-card {
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

.members {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

.members li {
  font-size: 14px;
  margin-bottom: 5px;
}

.leaderboard-card .v-card__title {
  font-size: 20px;
  font-weight: bold;
}

.team-info {
  padding: 16px;
}

.team-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.team-name {
  font-size: 18px;
  font-weight: bold;
}

.team-points {
  color: #555;
}

.team-members {
  margin-top: 8px;
}

.team-members-label {
  font-weight: bold;
  margin-bottom: 4px;
}

.team-members-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.team-members-list li {
  font-size: 14px;
  margin-bottom: 4px;
}

.highlighted {
  background-color: #090e18 !important;
}
</style>
