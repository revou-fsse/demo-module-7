// Insert regions and capture the inserted IDs
const region1 = db.regions.insertOne({
  regionName: "Australia",
});

const region2 = db.regions.insertOne({
  regionName: "South America",
});

// Insert customers using the inserted region _id values
const customer1 = db.customers.insertOne({
  name: "Ahmad Naufal",
  regionId: region1.insertedId,
  address: {
    address1: "Jl. Cikutra No. 1",
    address2: "Bandung",
  },
});

const customer2 = db.customers.insertOne({
  name: "Cik Maya",
  regionId: region2.insertedId,
  address: {
    address1: "Jl. Ciputri",
    address2: "Bekasi",
  },
});

// Insert orders using the inserted customer _id values
db.orders.insertOne({
  product: "Smartphone",
  customerId: customer1.insertedId,
});

db.orders.insertOne({
  product: "Laptop",
  customerId: customer2.insertedId,
});

db.orders.insertOne({
  product: "Smartwatch",
  customerId: customer2.insertedId,
});

// get all orders
db.orders.find();

// get all orders where product is 'Smartwatch'
db.orders.find({
  product: "Smartwatch",
});

// join using aggregate
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "customer",
    },
  },
]);

// update order
db.orders.updateOne(
  {
    product: "Smartwatch",
  },
  {
    $set: {
      product: "Smartwatch 2020",
    },
  }
);

// update many customers
db.orders.updateMany(
  {
    customerId: customer2.insertedId,
  },
  {
    $set: {
      product: "Smartwatch 2020",
    },
  }
);

// using or
db.customers.find({
  $or: [
    {
      name: "Ahmad Naufal",
    },
    {
      name: "Cik Rizal",
    },
  ],
});
