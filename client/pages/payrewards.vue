<template>
    <v-container>
      <h1>Pay Rewards</h1>
      <h2>List of Students</h2>
      <v-list>
        <v-list-item v-for="student in students" :key="student.id">
          <v-list-item-content>{{ student.name }}</v-list-item-content>
          <v-list-item-action>
            <v-btn outlined color="primary" @click="payReward(student.id)">
              Pay
            </v-btn>
          </v-list-item-action>
        </v-list-item>
      </v-list>
  
      <v-dialog v-model="dialog" max-width="400">
        <template v-slot:activator="{ on }"></template>
        <v-card>
          <v-card-title class="headline">Make Payment</v-card-title>
          <v-card-text>
            <!-- Payment form or details here -->
            <v-text-field v-model="upiId" label="UPI ID"></v-text-field>
            <br> <!-- Add a line break -->
            <v-text-field v-model="paymentAmount" label="Payment Amount"></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="processPayment">Pay Now</v-btn>
            <v-btn color="error" @click="dialog = false">Cancel</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        students: [
          { id: 1, name: "Student 1" },
          { id: 2, name: "Student 2" },
          { id: 3, name: "Student 3" },
          // Add more students here...
        ],
        dialog: false,
        upiId: "",
        paymentAmount: ""
      };
    },
    methods: {
      payReward(studentId) {
        // Set the selected student ID and open the payment dialog
        this.selectedStudentId = studentId;
        this.dialog = true;
      },
      processPayment() {
        // Perform the payment logic here
        // You can access the selectedStudentId, upiId, and paymentAmount data
        console.log("Selected Student ID:", this.selectedStudentId);
        console.log("UPI ID:", this.upiId);
        console.log("Payment Amount:", this.paymentAmount);
        // Implement your payment logic here
  
        // Clear the UPI ID and payment amount fields
        this.upiId = "";
        this.paymentAmount = "";
  
        // Close the payment dialog
        this.dialog = false;
      }
    }
  };
  </script>
  