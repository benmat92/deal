import React, { useState, useEffect } from 'react';
import {
  Grid,
  Card,
  CardActionArea,
  CardContent,
  CardMedia,
  Typography,
  Container,
  Chip
} from '@mui/material';

function Deals() {
  const [deals, setDeals] = useState([]);

  useEffect(() => {
    // Fetch the deals from your Django API
    fetch("http://127.0.0.1:8000/deals/")  // Adjust the endpoint URL
      .then(response => response.json())
      .then(data => setDeals(data));
  }, []);
  const cardStyle = {
    display: 'flex',
    flexDirection: 'column',
    height: '350px',  // An arbitrary height; adjust as per your requirement.
  };

  const cardMediaStyle = {
    height: '140px',
  };

  const cardContentStyle = {
    height: '220px',  // This is 400 (card height) - 140 (image) - 40 (for price) = 220px
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'space-between'
  };

  const priceStyle = {
    height: '40px',  // Allocate a fixed space for the price
  };

  return (
    <Container maxWidth="md" component="main">
      <Grid container spacing={4}>
        {deals.map((deal) => (
          <Grid item xs={12} sm={6} md={4} key={deal.id}>
            <Card style={cardStyle}>
              <CardActionArea>
                <CardMedia
                  component="img"
                  style={cardMediaStyle}
                  alt={deal.title}
                  height="140"
                  image={deal.header_image}  // Assuming the deal object has an 'image' field
                  title={deal.title}
                />
                <CardContent style={cardContentStyle}>

                    <Typography gutterBottom variant="h5" component="div">
                      {deal.title}
                    </Typography>
                    <Typography variant="body2" color="textSecondary" component="p">
                      {deal.excerpt}
                    </Typography>
                  <div style={priceStyle}>
                    <Chip
                      label={`$${deal.price}`}
                      color="primary"
                    />
                  </div>

                </CardContent>
              </CardActionArea>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>

  );
}

export default Deals;
