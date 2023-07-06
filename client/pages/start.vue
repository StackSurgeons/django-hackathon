<template>
  <v-container>
    <!-- Overview Card Row -->
    <v-layout row class="mb-4 mt-4">
      <v-flex xs4>
        <v-card class="overview-card">
          <v-card-title class="justify-start">Overview</v-card-title>
          <v-card-text>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec
            fringilla mauris.
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
          <v-card-text> Total registered users: 500 </v-card-text>
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
              <v-card-title class="title">Leaderboard</v-card-title>
              <v-divider></v-divider>
              <v-list class="leaderboard-list">
                <v-list-item v-for="team in leaderboardEntries" :key="team.id">
                  <v-list-item-content class="team-info">
                    <div
                      :class="{
                        'team-header': true,
                        highlighted: team.highlighted,
                      }"
                    >
                      <p class="team-name">{{ team.name }}</p>
                      <p class="team-points">{{ team.points }} points</p>
                    </div>
                    <div class="team-members">
                      <ul class="team-members-list">
                        <li v-for="member in team.members" :key="member">
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
          <v-card-title class="justify-start">Active Hackathons</v-card-title>
          <v-card-text> Number of active hackathons: 5 </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios"
export default {
  data() {
    return {
      leaderboardEntries: [
        {
          id: 1,
          name: "User A",
          points: 100,
          members: ["Member 1", "Member 2"],
          highlighted: true,
        },
        {
          id: 2,
          name: "User B",
          points: 85,
          members: ["Member 3", "Member 4"],
          highlighted: false,
        },
        {
          id: 3,
          name: "User C",
          points: 75,
          members: ["Member 5", "Member 6"],
          highlighted: false,
        },
        {
          id: 4,
          name: "User D",
          points: 65,
          members: ["Member 7", "Member 8"],
          highlighted: true,
        },
        {
          id: 5,
          name: "User E",
          points: 50,
          members: ["Member 9", "Member 10"],
          highlighted: true,
        },
      ],
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/company/dashboard/");
        this.leaderboardEntries = response.data;
        console.log(response.data)
      } catch (error) {
        console.error(error);
      }
    }
  }
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
