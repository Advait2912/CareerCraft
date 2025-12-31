const healthCheck = (req, res) => {
  res.status(200).json({
    status: "OK",
    message: "CareerCraft backend is running",
  });
};

export { healthCheck };
